import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'KeltnerChannels': 1.0
        })
    )
