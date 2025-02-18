import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'KeltnerChannels': 1.0
        })
    )
