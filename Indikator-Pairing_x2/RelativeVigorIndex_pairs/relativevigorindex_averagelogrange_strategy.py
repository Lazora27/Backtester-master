import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'AverageLogRange': 1.0
        })
    )
