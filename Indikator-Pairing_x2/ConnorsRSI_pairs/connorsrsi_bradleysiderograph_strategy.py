import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'BradleySiderograph': 1.0
        })
    )
