import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und FisherSignals
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'FisherSignals': 1.0
        })
    )
