import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DPOCycles_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DPOCycles und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'DPOCycles': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
