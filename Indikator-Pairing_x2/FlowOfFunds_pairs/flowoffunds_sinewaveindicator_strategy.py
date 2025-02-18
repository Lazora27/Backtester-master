import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
