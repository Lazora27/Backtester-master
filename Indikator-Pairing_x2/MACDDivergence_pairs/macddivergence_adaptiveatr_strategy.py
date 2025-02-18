import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'AdaptiveATR': 1.0
        })
    )
