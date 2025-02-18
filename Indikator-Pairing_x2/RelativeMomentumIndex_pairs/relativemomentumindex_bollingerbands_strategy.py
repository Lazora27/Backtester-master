import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und BollingerBands
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'BollingerBands': 1.0
        })
    )
