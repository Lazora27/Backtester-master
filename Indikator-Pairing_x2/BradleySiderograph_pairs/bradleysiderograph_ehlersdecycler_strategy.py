import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'EhlersDecycler': 1.0
        })
    )
