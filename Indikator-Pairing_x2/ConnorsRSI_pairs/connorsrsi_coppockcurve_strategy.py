import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'CoppockCurve': 1.0
        })
    )
