import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersInstantaneousTrendline_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersInstantaneousTrendline und TrendCycles
    """
    
    params = (
        ('indicators', {
            'EhlersInstantaneousTrendline': {
                'class': EhlersInstantaneousTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersInstantaneousTrendline'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'EhlersInstantaneousTrendline': 1.0,
            'TrendCycles': 1.0
        })
    )
