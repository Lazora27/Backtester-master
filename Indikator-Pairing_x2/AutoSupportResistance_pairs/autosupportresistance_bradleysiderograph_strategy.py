import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'BradleySiderograph': 1.0
        })
    )
