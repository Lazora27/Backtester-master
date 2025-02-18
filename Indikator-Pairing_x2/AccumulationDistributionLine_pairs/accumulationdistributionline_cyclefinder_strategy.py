import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und CycleFinder
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'CycleFinder': 1.0
        })
    )
