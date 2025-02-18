import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und MassIndex
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'MassIndex': 1.0
        })
    )
