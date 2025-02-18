import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_EhlersInstantaneousTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und EhlersInstantaneousTrendline
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'EhlersInstantaneousTrendline': {
                'class': EhlersInstantaneousTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersInstantaneousTrendline'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'EhlersInstantaneousTrendline': 1.0
        })
    )
