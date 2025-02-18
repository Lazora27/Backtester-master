import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'KeltnerChannels': 1.0
        })
    )
