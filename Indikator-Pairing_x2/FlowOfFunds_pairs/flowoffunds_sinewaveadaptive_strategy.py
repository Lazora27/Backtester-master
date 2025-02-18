import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
