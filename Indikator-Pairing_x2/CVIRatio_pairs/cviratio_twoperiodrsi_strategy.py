import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
