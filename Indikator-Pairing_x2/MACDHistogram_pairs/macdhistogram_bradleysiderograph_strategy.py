import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'BradleySiderograph': 1.0
        })
    )
