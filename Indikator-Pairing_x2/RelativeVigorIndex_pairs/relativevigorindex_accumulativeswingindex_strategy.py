import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_AccumulativeSwingIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und AccumulativeSwingIndex
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'AccumulativeSwingIndex': {
                'class': AccumulativeSwingIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulativeSwingIndex'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'AccumulativeSwingIndex': 1.0
        })
    )
