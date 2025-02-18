import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_EhlersInstantaneousTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und EhlersInstantaneousTrendline
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'EhlersInstantaneousTrendline': {
                'class': EhlersInstantaneousTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersInstantaneousTrendline'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'EhlersInstantaneousTrendline': 1.0
        })
    )
