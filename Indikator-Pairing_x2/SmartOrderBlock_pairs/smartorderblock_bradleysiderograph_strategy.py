import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'BradleySiderograph': 1.0
        })
    )
