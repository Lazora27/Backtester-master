import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'AutoFibonacci': 1.0
        })
    )
