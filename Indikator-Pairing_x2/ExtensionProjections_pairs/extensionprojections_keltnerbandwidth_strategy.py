import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
