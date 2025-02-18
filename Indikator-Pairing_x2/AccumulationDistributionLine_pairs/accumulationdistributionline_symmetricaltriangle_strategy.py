import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
