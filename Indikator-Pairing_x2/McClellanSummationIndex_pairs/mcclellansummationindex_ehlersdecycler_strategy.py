import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'EhlersDecycler': 1.0
        })
    )
