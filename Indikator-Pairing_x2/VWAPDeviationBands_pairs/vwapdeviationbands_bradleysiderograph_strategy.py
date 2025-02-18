import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'BradleySiderograph': 1.0
        })
    )
