import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'BradleySiderograph': 1.0
        })
    )
