import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'HilbertTrendline': 1.0
        })
    )
