import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'BradleySiderograph': 1.0
        })
    )
