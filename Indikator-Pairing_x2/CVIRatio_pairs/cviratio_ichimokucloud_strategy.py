import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'IchimokuCloud': 1.0
        })
    )
