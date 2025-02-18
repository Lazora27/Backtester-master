import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'DPOCycles': 1.0
        })
    )
