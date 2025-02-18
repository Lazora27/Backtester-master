import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
