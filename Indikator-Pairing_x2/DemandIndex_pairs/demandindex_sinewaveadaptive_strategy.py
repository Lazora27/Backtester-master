import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandIndex_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandIndex und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'DemandIndex': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
