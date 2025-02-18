import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_AdaptiveRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und AdaptiveRSI
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'AdaptiveRSI': 1.0
        })
    )
