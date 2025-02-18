import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
