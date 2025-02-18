import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
