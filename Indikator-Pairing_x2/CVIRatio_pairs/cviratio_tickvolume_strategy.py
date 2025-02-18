import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_TickVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und TickVolume
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'TickVolume': 1.0
        })
    )
