import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
