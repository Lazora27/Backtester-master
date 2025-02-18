import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandIndex_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandIndex und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'DemandIndex': 1.0,
            'EhlersDecycler': 1.0
        })
    )
