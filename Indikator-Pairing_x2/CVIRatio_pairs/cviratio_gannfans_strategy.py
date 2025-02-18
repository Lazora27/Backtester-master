import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und GannFans
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'GannFans': 1.0
        })
    )
