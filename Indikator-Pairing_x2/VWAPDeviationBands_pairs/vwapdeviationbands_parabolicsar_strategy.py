import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'ParabolicSAR': 1.0
        })
    )
