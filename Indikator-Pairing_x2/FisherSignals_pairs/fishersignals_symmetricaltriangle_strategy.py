import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherSignals_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherSignals und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'FisherSignals': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
