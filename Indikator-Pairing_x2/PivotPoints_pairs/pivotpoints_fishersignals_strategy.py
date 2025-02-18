import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und FisherSignals
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'FisherSignals': 1.0
        })
    )
