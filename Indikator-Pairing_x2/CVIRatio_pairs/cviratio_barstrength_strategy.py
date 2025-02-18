import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und BarStrength
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'BarStrength': 1.0
        })
    )
