import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_ConnorsRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und ConnorsRSI
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'ConnorsRSI': 1.0
        })
    )
