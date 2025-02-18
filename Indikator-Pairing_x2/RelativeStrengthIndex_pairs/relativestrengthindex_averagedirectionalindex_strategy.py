import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
