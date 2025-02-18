import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
