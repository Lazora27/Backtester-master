import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'ModifiedATR': 1.0
        })
    )
