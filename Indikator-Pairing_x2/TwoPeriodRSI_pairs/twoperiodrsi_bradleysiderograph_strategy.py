import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'BradleySiderograph': 1.0
        })
    )
