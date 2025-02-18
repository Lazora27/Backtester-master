import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
