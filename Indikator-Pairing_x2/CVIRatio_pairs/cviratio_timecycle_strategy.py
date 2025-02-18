import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und TimeCycle
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'TimeCycle': 1.0
        })
    )
