import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'BradleySiderograph': 1.0
        })
    )
