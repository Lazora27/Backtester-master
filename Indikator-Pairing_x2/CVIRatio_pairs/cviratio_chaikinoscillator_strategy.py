import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_ChaikinOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und ChaikinOscillator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'ChaikinOscillator': 1.0
        })
    )
